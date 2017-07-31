n = nuke.selectedNode()


nwidth = n.width()
nheight = n.height()

# Setup values for the crop
#
BL = [0,0,nwidth/2,nheight/2]
BR = [(nwidth/2)+1,0,nwidth,nheight/2]
TR = [(nwidth/2)+1,(nheight/2)+1,nwidth,nheight]
TL = [0,(nheight/2)+1,nwidth/2,nheight]
MID = [nwidth*0.25, nheight*0.25, nwidth*0.75, nheight*0.75]
croplist = [BL,BR,TR,TL,MID]
# Setup values for reformat.
reformatknobs = [["type",1],["box_width",3],["box_height",3],["box_fixed","True"],["filter",8],["resize",5]]


# Lets create the crops with the correct sizes
for x in croplist:
  a = nuke.createNode("Crop")
  a["box"].setValue(x)
  a["reformat"].setValue(True)
  # connect it to the originally selected node
  a.setInput(0,n)
  # create reformat 3x3 pixels in size.
  reformat = nuke.createNode("Reformat")
  for y in reformatknobs:
    # set knobs based on the earlier list.
    reformat[y[0]].setValue(y[1])
# At this point I could add in the curvetool and grab the name so later I can execute it.
