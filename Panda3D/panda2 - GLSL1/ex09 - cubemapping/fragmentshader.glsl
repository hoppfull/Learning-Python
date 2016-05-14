#version 330

layout (location = 0) out vec4 color;
uniform samplerCube cubemap01;

in VS_OUT {
    vec3 N;
    vec3 R;
} fs_in;

void main(){

    vec3 N = normalize(fs_in.N);
    vec4 texture = textureCube(cubemap01, fs_in.R);
    color = texture;
}