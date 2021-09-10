

from controller import Robot


robot = Robot()


timestep = int(robot.getBasicTimeStep())

time_step=16
max_speed=2


left_motor = robot.getMotor('wheel1')
right_motor = robot.getMotor('wheel2')
backleft_motor = robot.getMotor('wheel3')
backright_motor = robot.getMotor('wheel4')

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))
backleft_motor.setPosition(float('inf'))
backright_motor.setPosition(float('inf'))

left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)
backleft_motor.setVelocity(0.0)
backright_motor.setVelocity(0.0)


right_ir = robot.getDevice('ds_right')
right_ir.enable(time_step)

mid_ir= robot.getDevice('ds_mid')
mid_ir.enable(time_step)

left_ir = robot.getDevice('ds_left')
left_ir.enable(time_step)



while robot.step(time_step) != -1:
    
    right_ir_val = right_ir.getValue()
    mid_ir_val = mid_ir.getValue()
    left_ir_val = left_ir.getValue()
    
    
    print("left: {} mid: {} right: {}".format(left_ir_val, mid_ir_val, right_ir_val))
    
    left_speed = max_speed
    right_speed = max_speed
    
    if left_ir_val>500 and right_ir_val>500 and mid_ir_val>=510:
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
        
        
    if left_ir_val<500 and right_ir_val>=500 and mid_ir_val>=500:
        left_motor.setVelocity(left_speed)
        backleft_motor.setVelocity(left_speed)
        right_motor.setVelocity(0)
        backright_motor.setVelocity(0)
        
    if left_ir_val>=500 and right_ir_val<500 and mid_ir_val>=500:
        left_motor.setVelocity(0)
        backleft_motor.setVelocity(0)
        right_motor.setVelocity(right_speed)
        backright_motor.setVelocity(right_speed)
        
    
    
    
    
    pass


