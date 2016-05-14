#version 330

layout (location = 0) in vec3 pos1;
layout (location = 1) in vec3 pos2;

uniform mat4 my_ModelMatrix;
uniform mat4 my_ViewMatrix;

void main(){
    gl_Position = my_ViewMatrix * my_ModelMatrix * vec4(pos1, 1.0);
}