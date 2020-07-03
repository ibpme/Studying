#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i=0; i<height ; i++)
    {
        for (int j=0; j<width ;j++)
        {
           int red = image[i][j].rgbtRed;
           int green = image[i][j].rgbtGreen;
           int blue = image[i][j].rgbtBlue;
           int gray = (red + green + blue)/3;
           image[i][j].rgbtRed= gray;
           image[i][j].rgbtGreen=gray;
           image[i][j].rgbtBlue=gray;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i=0; i<height ; i++)
    {
        for (int j=0; j<width ;j++)
        {
           int sepiaRed = 0.393*image[i][j].rgbtRed + 0.769*image[i][j].rgbtGreen + 0.189*image[i][j].rgbtBlue;
           int sepiaGreen = 0.349*image[i][j].rgbtRed + 0.686*image[i][j].rgbtGreen + 0.168*image[i][j].rgbtBlue;
           int sepiaBlue = 0.272*image[i][j].rgbtRed + 0.534*image[i][j].rgbtGreen + 0.131*image[i][j].rgbtBlue;
           if (sepiaBlue > 255)
           {
               sepiaBlue=255;
           }
            if (sepiaRed > 255)
           {
               sepiaRed=255;
           }
            if (sepiaGreen > 255)
           {
               sepiaGreen=255;
           }
           image[i][j].rgbtRed= sepiaRed;
           image[i][j].rgbtGreen=sepiaGreen;
           image[i][j].rgbtBlue=sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int m;
    int reflectRed[height][width];
    int reflectBlue[height][width];
    int reflectGreen[height][width];

    for (int i=0; i<height ; i++)
    {
        for (int j=1; j<width ;j++)
        {
            m = width-j;
            reflectRed[i][j] = image[i][m].rgbtRed;
            reflectGreen[i][j] = image[i][m].rgbtGreen;
            reflectBlue[i][j] = image[i][m].rgbtBlue;
        }
    }
    for (int i=0; i<height ; i++)
    {
        for (int j=1; j<width ;j++)
        {
            image[i][j].rgbtRed=reflectRed[i][j];
            image[i][j].rgbtGreen=reflectGreen[i][j];
            image[i][j].rgbtBlue=reflectBlue[i][j];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    int blurRed[height][width];
    int blurBlue[height][width];
    int blurGreen[height][width];

    for (int i=0; i<height ; i++)
    {
        for (int j=0; j<width ;j++)
        {
            if(i>1 && j>1 && i<height-1 && j<width-1 )
            {
                blurRed[i][j] = (image[i][j].rgbtRed+image[i+1][j].rgbtRed+image[i-1][j].rgbtRed+image[i][j+1].rgbtRed+image[i][j-1].rgbtRed+image[i+1][j+1].rgbtRed+image[i-1][j-1].rgbtRed+image[i+1][j-1].rgbtRed+image[i-1][j+1].rgbtRed)/9;
                blurGreen[i][j] = (image[i][j].rgbtGreen+image[i+1][j].rgbtGreen+image[i-1][j].rgbtGreen+image[i][j+1].rgbtGreen+image[i][j-1].rgbtGreen+image[i+1][j+1].rgbtGreen+image[i-1][j-1].rgbtGreen+image[i+1][j-1].rgbtGreen+image[i-1][j+1].rgbtGreen)/9;
                blurBlue[i][j] = (image[i][j].rgbtBlue+image[i+1][j].rgbtBlue+image[i-1][j].rgbtBlue+image[i][j+1].rgbtBlue+image[i][j-1].rgbtBlue+image[i+1][j+1].rgbtBlue+image[i-1][j-1].rgbtBlue+image[i+1][j-1].rgbtBlue+image[i-1][j+1].rgbtBlue)/9;
            }

        }
    }
    return;
    for (int i=0; i<height ; i++)
    {
        for (int j=1; j<width ;j++)
        {
            image[i][j].rgbtRed=blurRed[i][j];
            image[i][j].rgbtGreen=blurGreen[i][j];
            image[i][j].rgbtBlue=blurBlue[i][j];
        }
    }
    return;
}
