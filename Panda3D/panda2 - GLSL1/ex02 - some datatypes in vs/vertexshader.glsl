#version 330

in vec4 p3d_Vertex;
uniform mat4 p3d_ModelViewProjectionMatrix;

//Datatypes:
float f = 10.0;     //Float
int i = 10;         //Integer
bool b = true;      //Boolean

vec2 v2 = vec2(1.0, 1.0);           //Vector in R^2
vec3 v3 = vec3(1.0, 1.0, 1.0);      //Vector in R^3
vec4 v4 = vec4(1.0, 1.0, 1.0, 1.0); //Vector in R^4
ivec4 iv4 = ivec4(1, 1, 1, 1);      //Vector in I^4
bvec4 bv4 = bvec4(true, true, false, true); //Apparently completely useless...

mat3 M3; //Matrix in R^(3*3), I don't know how to assign values though...

void main(){
    gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
}