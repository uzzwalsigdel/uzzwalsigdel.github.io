from PIL import Image; import glob
fs=sorted(glob.glob('pg-*.png')); print(len(fs))
for i in range(0,len(fs),6):
    ims=[Image.open(f) for f in fs[i:i+6]]; w,h=ims[0].size
    sheet=Image.new('RGB',(w*3,h*2),'white')
    for k,im in enumerate(ims): sheet.paste(im,((k%3)*w,(k//3)*h))
    sheet.save(f'sheet{i//6:02d}.png')
