#version 120

uniform float a;
uniform vec4 b;

void main(){
    gl_FragColor = b * a;
}