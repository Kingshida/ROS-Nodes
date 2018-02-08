# ROS-Nodes
Getting to know about ROS Nodes
Short descripion about packages

1. Package: "pub_pkg"
    -> Simple publisher and subscriber nodes. (in scripts folder)
    -> Using genereic message file. (saved in msg folder)

2. Package: "depend_pkg"
    -> Node which uses a user defined message file present in different package (in "pub_pkg" package)

3. Package: "turtlesim_node_demo"
    -> Node to publish velocity information ("Twist" message type).
    -> Can be visualised by running publisher node written (present in scripts) parallely with "turtlesim_node"
    -> Subscriber node which sunscribes to "/cmd_vel" topic and saves the data in a ".xls" file (in home folder)
