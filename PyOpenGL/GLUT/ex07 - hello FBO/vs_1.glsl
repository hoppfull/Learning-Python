#version 330

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 uvcoord0;

out vec2 texcoord0;

void main(){
    texcoord0 = uvcoord0;
    gl_Position = vec4(position*0.5, 1.0);
}