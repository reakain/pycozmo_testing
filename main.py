#!/usr/bin/env python

import time

from PIL import Image
import numpy as np
import pycozmo

def on_robot_state(cli, pkt: pycozmo.protocol_encoder.RobotState):
    print("Battery level: {:.01f} V".format(pkt.battery_voltage))


def on_robot_poked(cli, pkt: pycozmo.protocol_encoder.RobotPoked):
    print("Robot poked.")


def on_robot_picked_up(cli, state: bool):
    if state:
        print("Picked up.")
    else:
        print("Put down.")


def on_robot_charging(cli, state: bool):
    if state:
        print("Started charging.")
    else:
        print("Stopped charging.")


def on_cliff_detected(cli, state: bool):
    if state:
        print("Cliff detected.")


def on_robot_orientation_change(cli, orientation: pycozmo.robot.RobotOrientation):
    if orientation == pycozmo.robot.RobotOrientation.ON_THREADS:
        print("On threads.")
    elif orientation == pycozmo.robot.RobotOrientation.ON_BACK:
        print("On back.")
    elif orientation == pycozmo.robot.RobotOrientation.ON_FACE:
        print("On front.")
    elif orientation == pycozmo.robot.RobotOrientation.ON_LEFT_SIDE:
        print("On left side.")
    elif orientation == pycozmo.robot.RobotOrientation.ON_RIGHT_SIDE:
        print("On right side.")

def on_animation_complete(cli, state:bool):
    if state:
        print("Animation complete")
    else:
        print("still going")


def main(command, option):
    if command == "pexpressions":
        for expression in pycozmo.expressions.expressions.__all__:
            print(expression, flush=True)
    elif command == "panims":
        pcli = pycozmo.Client()
        pcli.load_anims()
        for name in sorted(pcli.get_anim_names()):
            print(name, flush=True)
    elif command == "panimgroups":
        pcli = pycozmo.Client()
        pcli.load_anims()
        groups = pcli.animation_groups
        for group in groups:
            print(group, flush=True)
    elif command == "expression" and option not in pycozmo.expressions.expressions.__all__:
        print("ERROR: " + option + " is not a valid expression.", flush=True)
    else:
        with pycozmo.connect() as cli:

            cli.add_handler(pycozmo.event.EvtRobotPickedUpChange, on_robot_picked_up)
            cli.add_handler(pycozmo.protocol_encoder.RobotState, on_robot_state, one_shot=True)
            cli.add_handler(pycozmo.event.EvtRobotOrientationChange, on_robot_orientation_change)
            cli.add_handler(pycozmo.protocol_encoder.RobotPoked, on_robot_poked)
            cli.add_handler(pycozmo.event.EvtCliffDetectedChange, on_cliff_detected)
            cli.add_handler(pycozmo.event.EvtRobotChargingChange, on_robot_charging)
            #cli.add_handler(pycozmo.event.EvtAnimationCompleted, on_animation_complete)

            # Load animations - one time.
            cli.load_anims()

            if command == "tanim":
                if option in cli.get_anim_names():
                    # Play an animation.
                    cli.play_anim(option)
                    cli.wait_for(pycozmo.event.EvtAnimationCompleted)
                    time.sleep(3)
                else:
                    print ("ERROR: " + option + " is not a valid animation.", flush=True)

            elif command == "tanimgroup":
                if option in cli.animation_groups:
                    # Play animation group
                    cli.play_anim_group(option)
                    cli.wait_for(pycozmo.event.EvtAnimationCompleted)
                    time.sleep(3)
                else:
                    print ("ERROR: " + option + " is not a valid animation group.", flush=True)

            elif command =="tcompound":
                time.sleep(2)
                cli.drive_wheels(100, -100, lwheel_acc=999, rwheel_acc=999, duration = 0.3)
                cli.drive_wheels(-100, 100, lwheel_acc=999, rwheel_acc=999, duration = 0.6)
                cli.drive_wheels(100, -100, lwheel_acc=999, rwheel_acc=999, duration = 0.4)
                cli.move_head(1)
                time.sleep(1)
                cli.drive_wheels(100, -100, lwheel_acc=999, rwheel_acc=999, duration = 0.3)
                cli.drive_wheels(-100, 100, lwheel_acc=999, rwheel_acc=999, duration = 0.6)
                cli.drive_wheels(100, -100, lwheel_acc=999, rwheel_acc=999, duration = 0.4)
                time.sleep(1)
                cli.play_anim_group("CodeLabChatty")
                cli.play_anim_group("VC_Alrighty")
                time.sleep(2)


            elif command == "expressions" or "expression":
                cli.enable_procedural_face(False)
                # Raise head.
                angle = (pycozmo.robot.MAX_HEAD_ANGLE.radians - pycozmo.robot.MIN_HEAD_ANGLE.radians) / 2.0
                cli.set_head_angle(angle)
                time.sleep(1)

                # List of face expressions.
                expressions = [
                    pycozmo.expressions.Anger(),
                    pycozmo.expressions.Sadness(),
                    pycozmo.expressions.Happiness(),
                    pycozmo.expressions.Surprise(),
                    pycozmo.expressions.Disgust(),
                    pycozmo.expressions.Fear(),
                    pycozmo.expressions.Pleading(),
                    pycozmo.expressions.Vulnerability(),
                    pycozmo.expressions.Despair(),
                    pycozmo.expressions.Guilt(),
                    pycozmo.expressions.Disappointment(),
                    pycozmo.expressions.Embarrassment(),
                    pycozmo.expressions.Horror(),
                    pycozmo.expressions.Skepticism(),
                    pycozmo.expressions.Annoyance(),
                    pycozmo.expressions.Fury(),
                    pycozmo.expressions.Suspicion(),
                    pycozmo.expressions.Rejection(),
                    pycozmo.expressions.Boredom(),
                    pycozmo.expressions.Tiredness(),
                    pycozmo.expressions.Asleep(),
                    pycozmo.expressions.Confusion(),
                    pycozmo.expressions.Amazement(),
                    pycozmo.expressions.Excitement(),
                ]

                # Base face expression.
                base_face = pycozmo.expressions.Neutral()

                rate = pycozmo.robot.FRAME_RATE
                timer = pycozmo.util.FPSTimer(rate)
                for expression in expressions:
                    if command == "expressions" or expression.__class__.__name__ == option:
                        # Transition from base face to expression and back.
                        for from_face, to_face in ((base_face, expression), (expression, base_face)):

                            if to_face != base_face:
                                print(to_face.__class__.__name__, flush=True)

                            # Generate transition frames.
                            face_generator = pycozmo.procedural_face.interpolate(from_face, to_face, rate // 3)
                            for face in face_generator:

                                # Render face image.
                                im = face.render()

                                # The Cozmo protocol expects a 128x32 image, so take only the even lines.
                                np_im = np.array(im)
                                np_im2 = np_im[::2]
                                im2 = Image.fromarray(np_im2)

                                # Display face image.
                                cli.display_image(im2)

                                # Maintain frame rate.
                                timer.sleep()

                            # Pause for 1s.
                            for i in range(rate):
                                timer.sleep()
                    

            

if __name__ == "__main__":
    import sys

    # Get what to test
    if len(sys.argv) == 2:
        command = str(sys.argv[1])
        if command =="expressions" or \
            command == "panims" or \
            command =="pexpressions" or \
            command == "panimgroups" or \
            command == "tcompound":
            option = ""
        else:
            command = "-h"
    elif len(sys.argv) == 3:
        command = str(sys.argv[1])
        if command == "tanim" or \
            command =="expression" or\
            command == "tanimgroup":
            option = str(sys.argv[2])
        else:
            command = "-h"
    else:
        command = "-h"

    if command == "-h":
        print("Possible function tests are called with:")
        print("pexressions --------------- Print all expression names")
        print("expressions --------------- See all possible expressions and their names")
        print("expression <option> ------- Run expression with specific name")
        print("panims -------------------- Print all animation names")
        print("tanim <option> ------------ Run animation with specific name")
        print("panimgroups --------------- Print all animation group names")
        print("tanimgroup <option> ------- Run animation group with specific name")
        print("tcompound ----------------- Test a compound animation", flush=True)
    else:
        #Run as main program
        main(command, option)