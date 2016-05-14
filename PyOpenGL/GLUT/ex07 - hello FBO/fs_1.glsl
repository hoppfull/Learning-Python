#version 330

layout (location = 0) out vec4 fragColor;
in vec2 texcoord0;

uniform sampler2D tex0;

void main(){
    fragColor = texture2D(tex0, texcoord0);
}