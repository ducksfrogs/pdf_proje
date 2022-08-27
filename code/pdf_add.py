import glob
import shutil
import PyPDF2 as pd

arr = glob.glob('../src/*.pdf')
arr.sort

it = iter(arr)
nitr = int(len(arr)/2)

for i, j, k in zip(range(nitr), it, it):
    merger = pd.PdfMerger()
    merger.append(j)
    merger.append(k)
    merger.write(f'test{i}.pdf')
    merger.close()
    shutil.move(f'test{i}.pdf', '../dist/')

print("Done making pdf files")