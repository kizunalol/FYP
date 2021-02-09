#!/usr/bin/env python

import numpy as np

from pycrazyswarm import *
import uav_trajectory

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    traj1 = uav_trajectory.Trajectory()
    traj2 = uav_trajectory.Trajectory()
    traj3 = uav_trajectory.Trajectory()
    traj4 = uav_trajectory.Trajectory()
    traj5 = uav_trajectory.Trajectory()
    traj6 = uav_trajectory.Trajectory()
    traj7 = uav_trajectory.Trajectory()
    traj8 = uav_trajectory.Trajectory()
    traj9 = uav_trajectory.Trajectory()
    
    # upload first csv-----------------------------------------------------------------------
    traj1.loadcsv(".csv")
    traj2.loadcsv(".csv")
    traj3.loadcsv(".csv")
    traj4.loadcsv(".csv")
    traj5.loadcsv(".csv")
    traj6.loadcsv(".csv")
    traj7.loadcsv(".csv")
    traj8.loadcsv(".csv")
    traj9.loadcsv(".csv")
    
    move1 = uav_trajectory.Trajectory()
    move2 = uav_trajectory.Trajectory()
    move3 = uav_trajectory.Trajectory()
    move4 = uav_trajectory.Trajectory()
    move5 = uav_trajectory.Trajectory()
    move6 = uav_trajectory.Trajectory()
    move7 = uav_trajectory.Trajectory()
    move8 = uav_trajectory.Trajectory()
    move9 = uav_trajectory.Trajectory()  
    
    move1.loadcsv(".csv")
    move2.loadcsv(".csv")
    move3.loadcsv(".csv")
    move4.loadcsv(".csv")
    move5.loadcsv(".csv")
    move6.loadcsv(".csv")
    move7.loadcsv(".csv")
    move8.loadcsv(".csv")
    move9.loadcsv(".csv")
    
    ids=[1,2,3,4,5,6,7,8,9]
    
    T = 1
    TRIALS = 1
    TIMESCALE = 1.0
    for i in range(TRIALS):
        for cf in allcfs.crazyflies:
            cf.uploadTrajectory(T*1, 0, traj1)
            cf.uploadTrajectory(T*2, 0, traj2)
            cf.uploadTrajectory(T*3, 0, traj3)
            cf.uploadTrajectory(T*4, 0, traj4)
            cf.uploadTrajectory(T*5, 0, traj5)
            cf.uploadTrajectory(T*6, 0, traj6)
            cf.uploadTrajectory(T*7, 0, traj7)
            cf.uploadTrajectory(T*8, 0, traj8)
            cf.uploadTrajectory(T*9, 0, traj9)
        
        # take off
        allcfs.takeoff(targetHeight=1.0, duration=1.0)
        timeHelper.sleep(1.5)
        for cf in allcfs.crazyflies:
            pos = np.array(cf.initialPosition) + np.array([0, 0, 1.0])
            cf.goTo(pos, 0, 1.0)
        timeHelper.sleep(1.5)
        
        # excute first traj
        for cf in allcfs.crazyflies:
            cf.startTrajectory(cf.id-T*1)
        timeHelper.sleep(traj1.duration * TIMESCALE + 2.0)
        
        #allcfs.startTrajectory(0, timescale=TIMESCALE)
        #timeHelper.sleep(traj1.duration * TIMESCALE + 2.0)
        
    # upload second csv--------------------------------------------------------------------
    T = 2
    for i in range(TRIALS):
        for cf in allcfs.crazyflies:
            cf.uploadTrajectory(T*1, 0, move1)
            cf.uploadTrajectory(T*2, 0, move2)
            cf.uploadTrajectory(T*3, 0, move3)
            cf.uploadTrajectory(T*4, 0, move4)
            cf.uploadTrajectory(T*5, 0, move5)
            cf.uploadTrajectory(T*6, 0, move6)
            cf.uploadTrajectory(T*7, 0, move7)
            cf.uploadTrajectory(T*8, 0, move8)
            cf.uploadTrajectory(T*9, 0, move9)
            
        # excute second traj
        for cf in allcfs.crazyflies:
            cf.startTrajectory(cf.id-T*1)
        timeHelper.sleep(move1.duration * TIMESCALE + 2.0)
        
        #allcfs.startTrajectory(0, timescale=TIMESCALE)
        #timeHelper.sleep(move1.duration * TIMESCALE + 2.0)
        
        
        # land--------------------------------------------------------------------------------------
        allcfs.land(targetHeight=0.06, duration=2.0)
        timeHelper.sleep(3.0)
