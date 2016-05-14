#version 330

layout (location = 0) in vec3 pos1;
layout (location = 1) in vec3 pos2;

uniform mat4 my_ModelMatrix;
uniform mat4 my_ViewMatrix;
uniform mat4 my_ProjectionMatrix;

void main(){
    
    /* ModelViewProjectionMatrix: */
    gl_Position = my_ProjectionMatrix * my_ViewMatrix * my_ModelMatrix * vec4(pos2, 1.0);
}