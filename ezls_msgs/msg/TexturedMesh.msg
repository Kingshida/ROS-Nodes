Header header

#Triangle point list, first point has id 0
geometry_msgs/Point[] points

#Normal vectors for every point
geometry_msgs/Point[] normal

#RGB color for every point. Range: [0,1] (only used if useTexture=false)
geometry_msgs/Point[] color

#Triangle list, x: id of point1, y: id of point2, z: id of point3
geometry_msgs/Point[] triangleList

#Bool use texture
bool useTexture

#Texture coordinates for every point. Range: [0,1]
geometry_msgs/Point[] textureCoord

#Texture (encoding has to be: sensor_msgs::image_encodings::BGR8)
sensor_msgs/Image texture
