#version 330

out vec4 fragColor;

uniform float a;
uniform vec4 b;

void main(){
    fragColor = b * a;
}