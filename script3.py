from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file='template1', model_segment=('FIRST:A','LAST:A'))
aln.append_model(mdl, align_codes='template1', atom_files='template1.pdb')
aln.append(file='qseq1.ali', align_codes='qseq1')
aln.align2d()
aln.write(file='qseq1-template1.ali', alignment_format='PIR')
aln.write(file='qseq1-template1.pap', alignment_format='PAP')