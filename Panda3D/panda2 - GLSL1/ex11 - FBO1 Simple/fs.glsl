#version 330

layout (location = 0) out vec4 color;

in vec2 texcoord0;
uniform sampler2D p3d_Texture0;

void main(){
    color = texture2D(p3d_Texture0, texcoord0);
}