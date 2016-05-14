#version 330

//Texturing:
uniform sampler2D p3d_Texture0; //This stores the first image file
uniform sampler2D p3d_Texture1; //This stores the second image file
in vec2 texcoord0;              //This is the texture coordinate sent from the vertexshader for each vertex

void main(){
    gl_FragColor = vec4(texture2D( p3d_Texture1, texcoord0 ));
}
/*
    "texture2D" is a function that returns a vector4 with RGBA-data on an image at a given coordinate.
    Syntax: "texture2D(image, coordinate)"
*/