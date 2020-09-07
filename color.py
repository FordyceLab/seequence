# COLOR SCHEMES (http://acces.ens-lyon.fr/biotic/rastop/help/colour.htm)
from Bio.SeqUtils import seq1

aa_rasmol = {
'ASP': '#E60A0A',
'GLU': '#E60A0A',
'CYS': '#E6E600',
'MET': '#E6E600',
'LYS': '#145AFF',
'ARG': '#145AFF',
'SER': '#FA9600',
'THR': '#FA9600',
'PHE': '#3232AA',
'TYR': '#3232AA',
'ASN': '#00DCDC',
'GLN': '#00DCDC',
'GLY': '#EBEBEB',
'LEU': '#0F820F',
'VAL': '#0F820F',
'ILE': '#0F820F',
'ALA': '#C8C8C8',
'TRP': '#B45AB4',
'HIS': '#8282D2',
'PRO': '#DC9682'}
aa_rasmol = {seq1(k):v for k,v in aa_rasmol.items()}

aa_shapely = {
'ALA':'#8CFF8C',
'GLY':'#FFFFFF',
'LEU':'#455E45',
'SER':'#FF7042',
'VAL':'#FF8CFF',
'THR':'#B84C00',
'LYS':'#4747B8',
'ASP':'#A00042',
'ILE':'#004C00',
'ASN':'#FF7C70',
'GLU':'#660000',
'PRO':'#525252',
'ARG':'#00007C',
'PHE':'#534C42',
'GLN':'#FF4C4C',
'TYR':'#8C704C',
'HIS':'#7070FF',
'CYS':'#FFFF70',
'MET':'#B8A042',
'TRP':'#4F4600'}
aa_shapely = {seq1(k):v for k,v in aa_shapely.items()}

nt_std = {'A':'blue','T':'yellow','G':'green','C':'red'}
nt_gc =  {'A':'orange','T':'yellow','G':'purple','C':'violet'}
nt_shapely = {'A':'#A0A0FF','C':'#FF8C4B','G':'#FF7070','T':'#A0FFA0'}

def color_const(seq, c='black'):
  return [c]*len(seq)
def color_dict(seq, cd=nt_std, default='grey'):
  return [cd[char] if char in cd.keys() else default for char in seq]
