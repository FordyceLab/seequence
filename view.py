from color import *
import numpy as np

from bokeh.plotting import figure, show
from bokeh.models import HoverTool, LinearAxis, Segment
from bokeh.models import ColumnDataSource, Range1d, BasicTicker, CustomJS
from bokeh.models.glyphs import Text, Rect
from bokeh.transform import linear_cmap
from bokeh.models.annotations import ColorBar
from bokeh.events import DoubleTap
from bokeh.layouts import gridplot
from bokeh.resources import Resources
from bokeh.io import output_notebook
output_notebook(Resources(mode="cdn", components=["bokeh", "bokeh-gl"]))


def view_seq(seq, layer, start=0,scale=1, cd=None, xr=None):
  # DATA
  seq_l = len(seq)
  if cd == None:
    if scale==1:
      cd = nt_gc
    elif scale==3:
      cd = aa_rasmol
    else:
      cd = {}

  source = ColumnDataSource(dict(x_center_ax = scale*(np.arange(seq_l)+.5) + start,
                                 x_start_ax = scale*np.arange(seq_l) + start,
                                 y = [layer]*seq_l,
                                 char = list(seq),
                                 color = color_dict(seq, cd),
                                 alpha = np.ones(seq_l)))


  # FIGURE
  font_pt = 8
  f = figure(y_range=[layer],
            min_border=0, height=2*(font_pt), sizing_mode='stretch_width',
            tools='xpan,xwheel_zoom', active_scroll='xwheel_zoom', output_backend='webgl')
  f.add_tools(HoverTool(tooltips='@char $index (@x_start_ax{0})',
                        anchor='bottom_center', attachment='below',
                        names=['rects']))
  f.grid.visible = False
  if xr==None:
    f.x_range = Range1d(start-seq_l*.015,seq_l+start+seq_l*.015)
    f.xaxis.ticker = BasicTicker(min_interval=1, max_interval=10000, mantissas=[1,3], desired_num_ticks=24,num_minor_ticks=0)
    f.plot_height += 25
  else:
    f.x_range = xr
    f.xaxis.visible = False
  

  # GLYPHS
  rects = Rect(x='x_center_ax', y='y',
               width=scale, height=1,
               fill_color='color', fill_alpha=.25,
               line_color='color', line_alpha=.13)
  f.add_glyph(source, rects, name='rects')

  chars = Text(x='x_center_ax', y='y', text='char',
               text_align='center', text_baseline='middle',
               text_font='monospace', text_font_size=f'{font_pt}pt', 
               text_color='black', text_alpha='alpha')
  f.add_glyph(source, chars)


  # CALLBACK
  callback = CustomJS(args=dict(xr=f.x_range, source=source, f=f, font_pt=font_pt, scale=scale), code="""
                      var w = f.properties.inner_width.spec.value
                      var l = source.data['alpha'].length
                      var range = xr.end - xr.start
                      var px_per_char = w/range
                      
                      if (scale*px_per_char < font_pt){
                        source.data['alpha'] = new Array(l).fill(0)
                        source.change.emit()
                        }
                      
                      if (scale*px_per_char >= font_pt){
                        source.data['alpha'] = new Array(l).fill(1)
                        source.change.emit()
                        }
                      """)
  f.x_range.js_on_change('end', callback)
  f.js_on_change('inner_width', callback)
  f.js_on_event(DoubleTap, CustomJS(args=dict(f=f), code='f.reset.emit()'))

  return f
