#version 330

layout (location = 0) in vec3 pos1;
layout (location = 1) in vec3 pos2;

void main(){
    gl_Position = vec4(pos1*0.9, 1.0);
}