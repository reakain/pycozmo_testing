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


def main():
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

        # Print the names of all available animations.
        #names = cli.get_anim_names()
        #for name in sorted(names):
        #    print(name)

        while True:
            #cli.enable_procedural_face=False

            # Play an animation.
            cli.play_anim("anim_bored_01")
            cli.wait_for(pycozmo.event.EvtAnimationCompleted)
            #cli.enable_procedural_face = True
            time.sleep(3)

            # # Raise head.
            # angle = (pycozmo.robot.MAX_HEAD_ANGLE.radians - pycozmo.robot.MIN_HEAD_ANGLE.radians) / 2.0
            # cli.set_head_angle(angle)
            # time.sleep(1)

            # # List of face expressions.
            # expressions = [
            #     pycozmo.expressions.Anger(),
            #     pycozmo.expressions.Sadness(),
            #     pycozmo.expressions.Happiness(),
            #     pycozmo.expressions.Surprise(),
            #     pycozmo.expressions.Disgust(),
            #     pycozmo.expressions.Fear(),
            #     pycozmo.expressions.Pleading(),
            #     pycozmo.expressions.Vulnerability(),
            #     pycozmo.expressions.Despair(),
            #     pycozmo.expressions.Guilt(),
            #     pycozmo.expressions.Disappointment(),
            #     pycozmo.expressions.Embarrassment(),
            #     pycozmo.expressions.Horror(),
            #     pycozmo.expressions.Skepticism(),
            #     pycozmo.expressions.Annoyance(),
            #     pycozmo.expressions.Fury(),
            #     pycozmo.expressions.Suspicion(),
            #     pycozmo.expressions.Rejection(),
            #     pycozmo.expressions.Boredom(),
            #     pycozmo.expressions.Tiredness(),
            #     pycozmo.expressions.Asleep(),
            #     pycozmo.expressions.Confusion(),
            #     pycozmo.expressions.Amazement(),
            #     pycozmo.expressions.Excitement(),
            # ]

            # # Base face expression.
            # base_face = pycozmo.expressions.Neutral()

            # rate = pycozmo.robot.FRAME_RATE
            # timer = pycozmo.util.FPSTimer(rate)
            # for expression in expressions:

            #     # Transition from base face to expression and back.
            #     for from_face, to_face in ((base_face, expression), (expression, base_face)):

            #         if to_face != base_face:
            #             print(to_face.__class__.__name__)

            #         # Generate transition frames.
            #         face_generator = pycozmo.procedural_face.interpolate(from_face, to_face, rate // 3)
            #         for face in face_generator:

            #             # Render face image.
            #             im = face.render()

            #             # The Cozmo protocol expects a 128x32 image, so take only the even lines.
            #             np_im = np.array(im)
            #             np_im2 = np_im[::2]
            #             im2 = Image.fromarray(np_im2)

            #             # Display face image.
            #             cli.display_image(im2)

            #             # Maintain frame rate.
            #             timer.sleep()

            #         # Pause for 1s.
            #         for i in range(rate):
            #             timer.sleep()

if __name__ == "__main__":
  #Run as main program
  main()