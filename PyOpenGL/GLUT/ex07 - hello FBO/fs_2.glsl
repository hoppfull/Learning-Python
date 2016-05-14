#version 330

layout (location = 0) out vec4 fragColor;
in vec2 texcoord0;

uniform sampler2D col_tex;

void main(){
    fragColor = texture2D(col_tex, texcoord0);
}