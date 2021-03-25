# COLOR SCHEMES (http://acces.ens-lyon.fr/biotic/rastop/help/colour.htm)
aa_rasmol = {
 'A': '#C8C8C8',
 'C': '#E6E600',
 'D': '#E60A0A',
 'E': '#E60A0A',
 'F': '#3232AA',
 'G': '#EBEBEB',
 'H': '#8282D2',
 'I': '#0F820F',
 'K': '#145AFF',
 'L': '#0F820F',
 'M': '#E6E600',
 'N': '#00DCDC',
 'P': '#DC9682',
 'Q': '#00DCDC',
 'R': '#145AFF',
 'S': '#FA9600',
 'T': '#FA9600',
 'V': '#0F820F',
 'W': '#B45AB4',
 'Y': '#3232AA'}

aa_shapely = {
 'A': '#8CFF8C',
 'C': '#FFFF70',
 'D': '#A00042',
 'E': '#660000',
 'F': '#534C42',
 'G': '#FFFFFF',
 'H': '#7070FF',
 'I': '#004C00',
 'K': '#4747B8',
 'L': '#455E45',
 'M': '#B8A042',
 'N': '#FF7C70',
 'P': '#525252',
 'Q': '#FF4C4C',
 'R': '#00007C',
 'S': '#FF7042',
 'T': '#B84C00',
 'V': '#FF8CFF',
 'W': '#4F4600',
 'Y': '#8C704C'}

nt_std = {'A':'blue','T':'yellow','G':'green','C':'red'}
nt_gc =  {'A':'orange','T':'yellow','G':'purple','C':'violet'}
nt_shapely = {'A':'#A0A0FF','C':'#FF8C4B','G':'#FF7070','T':'#A0FFA0'}

def color_const(seq, c='black'):
  return [c]*len(seq)
def color_dict(seq, cd=nt_std, default='grey'):
  return [cd[char] if char in cd.keys() else default for char in seq]
