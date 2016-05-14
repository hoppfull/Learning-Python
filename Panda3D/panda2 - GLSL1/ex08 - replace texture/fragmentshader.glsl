#version 330

uniform sampler2D tex;
in vec2 texcoord0;

void main(){
    gl_FragColor = texture2D( tex, texcoord0 );
}