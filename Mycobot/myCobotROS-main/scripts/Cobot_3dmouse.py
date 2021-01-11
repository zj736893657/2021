import time, random
from pythonAPI.mycobot3 import MyCobot
from pythonAPI.common import Angle, Coord
import spacenavigator
import time
# import redis
# import msgpack

# r = redis.StrictRedis("192.168.1.95",6379,db=1)#the Server, default port is 6379

# def read(name):
#     return msgpack.unpackb(r.get(name)) #Unpack the data

# def write( key, value):
#     return r.set(key.encode('utf-8'), msgpack.dumps(value))

if __name__ == '__main__':

    mycobot = MyCobot()
    
    success = spacenavigator.open()
    print(success)
    # if success:
    #     while 1:
    #         state = spacenavigator.read()
    #         data = {}
    #         data["Position"]=[state.x, state.y, state.z,state.roll,state.pitch,state.yaw]
    #         print(state.x, state.y, state.z,state.roll,state.pitch,state.yaw)

    print('Start check api\n')
    # print()

    color_name = ['red', 'green', 'blue']
    color_code = ['ff0000', '00ff00', '0000ff']
    print('::ser_color()')
    i = random.randint(0, len(color_code) - 1)
    mycobot.set_color(color_code[i])
    print('==>set color {}\n'.format(color_name[i]))
    time.sleep(0.5)
    x=90
    y=100
    z=300
    r=0
    p=0
    ya=0
    # print('::get_angles()')
    # print('==> degrees: {}\n'.format(mycobot.get_angles()))
    # time.sleep(0.5)

    # print('::get_angles_of_radian()')
    # print('==> radians: {}\n'.format(mycobot.get_angles_of_radian()))
    # time.sleep(0.5)
    while 1:
        state = spacenavigator.read()
        x += state.x*15
        y += state.y*15
        z += state.z*15
        r += state.roll*15
        p += state.pitch*15
        ya +=state.yaw*15
        print(x,y,z,r,p,ya)
        data = {}
        data["Position"]=[state.x, state.y, state.z,state.roll,state.pitch,state.yaw]
        mycobot.send_coords([x, y, z, r, p, ya], 70, 0)
        print("next step")
        # mycobot.send_angles([state.x*160,state.y*50,state.z*90,state.roll*90,state.pitch*90,state.yaw*90], 80)
        # print(state.x*160, state.y*50, state.z*90,state.roll*90,state.pitch*90,state.yaw*90)
        # print('==> set angles [0,0,0,0,0,0], speed 80\n')
        time.sleep(0.5)
        # print("next step")

    # print('::send_angles_by_radian')
    # mycobot.send_angles_by_radian([1,1,1,1,1,1], 70)
    # print('==> set raidans [1,1,1,1,1,1], speed 70\n')
    # time.sleep(1.5)

    # print('::send_angle()')
    # mycobot.send_angle(Angle.J2.value, 10, 50)
    # print('==> angle: joint2, degree: 10, speed: 50\n')
    # time.sleep(1)

    print('::get_coords()')
    print('==> coords {}\n'.format(mycobot.get_coords()))
    time.sleep(0.5)

    # print('::send_coords()')
    # mycobot.send_coords([160, 160, 160, 0, 0, 0], 70, 0)
    # print('==> send coords [160,160,160,0,0,0], speed 70, mode 0\n')
    # time.sleep(2.5)

    # print('::send_coord()')
    # mycobot.send_coord(Coord.X.value, -40, 70)
    # print('==> send coord id: X, coord value: -40, speed: 70\n')
    # time.sleep(2)

    # print('::set_free_mode()')
    # mycobot.set_free_mode()
    # print('==> into free moving mode.')
    print('=== check end <==\n')
