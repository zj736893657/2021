# -*-coding:utf-8-*-
#pip install  pywinusb
import spacenavigator
import time


success = spacenavigator.open()
print(success)
if success:
  while 1:
    state = spacenavigator.read()
    data = {}
    data["Position"]=[state.x, state.y, state.z,state.roll,state.pitch,state.yaw]
    # print(state.x, state.y, state.z)
    # print("t",state.t) #time
    data["Button_left"]=state.buttons[0]
    data["Button_right"]=state.buttons[1]

    time.sleep(1)