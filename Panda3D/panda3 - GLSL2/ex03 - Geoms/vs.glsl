#version 330 core

uniform mat4 p3d_ModelViewProjectionMatrix;

in vec3 vertex;
in vec3 hello;

void main(){
    gl_Position = p3d_ModelViewProjectionMatrix * vec4(hello, 1.0);
}