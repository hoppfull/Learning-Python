#version 330

out vec4 fragColor;

uniform float a;
uniform vec4 b;
uniform sampler2D s;
uniform sampler2D t;

in vec2 texcoord0;

void main(){
    fragColor = texture2D(s, texcoord0);
}