#version 330

layout (location = 0) in vec3 position;

uniform mat4 my_ModelMatrix;
uniform mat4 my_ViewMatrix;
uniform mat4 my_ProjectionMatrix;

void main(){
    
    /* ModelViewProjectionMatrix: */
    gl_Position = my_ProjectionMatrix * my_ViewMatrix * my_ModelMatrix * vec4(position, 1.0);
}