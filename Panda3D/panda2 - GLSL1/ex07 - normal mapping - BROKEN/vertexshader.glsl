#version 330

in vec4 p3d_Vertex;
in vec3 p3d_Tangent;
in vec3 p3d_Binormal;
in vec3 p3d_Normal;
uniform mat4 p3d_ModelViewProjectionMatrix;
uniform mat4 p3d_ModelViewMatrix; //Makes coordintes relative to view
uniform mat4 p3d_ModelMatrixInverse; //Makes coordinates relative to world
uniform mat3 p3d_NormalMatrix;
in vec2 p3d_MultiTexCoord0;

out VS_OUT {
    vec2 texcoord0;
    vec3 V;
    vec3 L;
} vs_out;

vec4 LightPos = vec4(0.0, -1.0, 1.0, 1.0);

void main(){
    vs_out.texcoord0 = p3d_MultiTexCoord0;
    
    vec3 T = normalize(p3d_NormalMatrix * p3d_Tangent);
    vec3 B = normalize(p3d_NormalMatrix * p3d_Binormal);
    vec3 N = normalize(p3d_NormalMatrix * p3d_Normal);
    
    vec3 L = p3d_NormalMatrix * (p3d_ModelMatrixInverse * LightPos).xyz;
    vs_out.L = vec3(dot(L, T), dot(L, B), dot(L, N));
    
    vec3 V = -(p3d_ModelViewMatrix * p3d_Vertex).xyz;
    vs_out.V = vec3(dot(V, T), dot(V, B), dot(V, N));
    
    gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
}