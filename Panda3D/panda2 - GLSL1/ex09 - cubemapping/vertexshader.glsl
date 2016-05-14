#version 330

in vec4 p3d_Vertex;
in vec3 p3d_Normal;
uniform mat4 p3d_ModelViewMatrixInverse;
uniform mat4 p3d_ModelViewProjectionMatrix;

out VS_OUT {
    vec3 N; //Normals in model coordinates
    vec3 R; //Refleced ray (eye2cubemap) in model coordinates
} vs_out;

void main(){
    vs_out.N = p3d_Normal;
    
    vec4 V = p3d_Vertex - p3d_ModelViewMatrixInverse * vec4(0.0, 0.0, 0.0, 1.0);
    vs_out.R = reflect(V.rgb, p3d_Normal);
    
    gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
}