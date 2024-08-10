#!/usr/bin/env python

import numpy as np
from roboticstoolbox.robot.Robot import Robot


class KinovaGen3(Robot):
    """
    Class that imports a KinovaGen3 URDF model

    ``KinovaGen3()`` is a class which imports a KinovaGen3 robot definition
    from a URDF file.  The model describes its kinematic and graphical
    characteristics.

    .. runblock:: pycon

        >>> import roboticstoolbox as rtb
        >>> robot = rtb.models.URDF.KinovaGen3()
        >>> print(robot)

    Defined joint configurations are:

    - qz, zero joint angle configuration, 'L' shaped configuration
    - qr, vertical 'READY' configuration
    - qs, arm is stretched out in the x-direction
    - qn, arm is at a nominal non-singular configuration

    .. codeauthor:: Jesse Haviland
    .. sectionauthor:: Peter Corke
    """

    def __init__(self):

        links, name, urdf_string, urdf_filepath = self.URDF_read(
            "kortex_description/robots/gen3.xacro"
        )

        super().__init__(
            links,
            name=name,
            manufacturer="Kinova",
            urdf_string=urdf_string,
            urdf_filepath=urdf_filepath,
            gripper_links=links[10],
        )

        # self.qdlim = np.array([
        # 2.1750, 2.1750, 2.1750, 2.1750, 2.6100, 2.6100, 2.6100, 3.0, 3.0])

        self.qr = np.deg2rad([0.0, 15.0, 180.0, 230.0, 0.0, 55.0, 90.0])
        self.qz = np.zeros(7)

        self.addconfiguration("qr", self.qr)
        self.addconfiguration("qz", self.qz)


if __name__ == "__main__":  # pragma nocover

    robot = KinovaGen3()
    robot.q = robot.qr
    print(robot)

    from swift import Swift

    env = Swift()
    env.launch()
    env.add(robot)
    env.hold()

    for link in robot.links:
        print("\n")
        print(link.isjoint)
