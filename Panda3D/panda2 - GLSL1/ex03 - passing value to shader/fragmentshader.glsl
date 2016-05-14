#version 330

uniform float x; //Entrypoint for the variable to the main program

void main(){
    gl_FragColor = vec4(x, 1, 1, 1);
}