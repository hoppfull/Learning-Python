#version 330

layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;
layout (location = 2) in vec2 uvcoord;

out vec2 texcoord0;

void main(){
    texcoord0 = uvcoord;
    gl_Position = vec4(position, 1.0);
}