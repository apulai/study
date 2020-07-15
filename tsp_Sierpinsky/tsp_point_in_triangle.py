


# Az A,B,C háromszögben keressük a P pontot
# Megrajzoljuk az AB, AC, AP egyeneseket, ha AP meredeksége a kettő meredekség között van, akkor benne van abban a siknegyedben
# Megrajzoljuk az BA, BC, BP egyeneseket, Ba AP meredeksége a kettő meredekség között van, akkor benne van abban a siknegyedben

ax=0
ay=0

bx=5
by=0

cx=2.6
cy=5

px=2
py=1.8

mAB=(by-ay)/(bx-ax)
mAP=(py-ay)/(px-ax)
mAC=(cy-ay)/(cx-ax)

mBA=(ay-by)/(ax-bx)
mBP=(py-by)/(px-bx)
mBC=(cy-by)/(cx-bx)

print("A: {},{}".format(ax,ay))
print("B: {},{}".format(bx,by))
print("C: {},{}".format(cx,cy))
print("P: {},{}".format(px,py))

APok = (mAB <= mAP <= mAC) or (mAC <= mAP <= mAB)
BPok = (mBA <= mBP <= mBC) or (mBC <= mBP <= mBA)

print("mAB:{} mAP:{} mAC:{} between:{}".format(mAB,mAP,mAC,APok))
print("mBA:{} mBP:{} mBC:{} between:{}".format(mBA,mBP,mBC,BPok))

