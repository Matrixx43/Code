#include <stdlib.h>
#include <math.h>
#include "helpers.h"

int THREE = 3;
int TWO = 2;

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int k = (int)round((float)(image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / THREE);
            image[i][j].rgbtBlue = k;
            image[i][j].rgbtGreen = k;
            image[i][j].rgbtRed = k;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int originalBlue = image[i][j].rgbtBlue;
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            //Set Blue
            if (.272 * originalRed + .534 * originalGreen + .131 * originalBlue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = (int)round((float).272 * originalRed + .534 * originalGreen + .131 * originalBlue);
            }
            //Set Green
            if (.349 * originalRed + .686 * originalGreen + .168 * originalBlue >= 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = (int)round((float).349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            }
            //Set Red
            if (.393 * originalRed + .769 * originalGreen + .189 * originalBlue >= 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = (int)round((float).393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int h = width / 2;
    for (int i = 0; i < height; i++)
    {
        int k = width - 1;
        for (int j = 0; j < h; j++)
        {
            int extra;
            //Blue
            extra = image[i][j].rgbtBlue;
            image[i][j].rgbtBlue = image[i][k].rgbtBlue;
            image[i][k].rgbtBlue = extra;
            //Green
            extra = image[i][j].rgbtGreen;
            image[i][j].rgbtGreen = image[i][k].rgbtGreen;
            image[i][k].rgbtGreen = extra;
            //Red
            extra = image[i][j].rgbtRed;
            image[i][j].rgbtRed = image[i][k].rgbtRed;
            image[i][k].rgbtRed = extra;
            k--;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //Blue temporary array
    int **arrB = (int **)malloc(3 * sizeof(int *));
    for (int i = 0; i < 3; i++)
    {
        arrB[i] = (int *)malloc(width * sizeof(int));
    }
    //Green temporary array
    int **arrG = (int **)malloc(3 * sizeof(int *));
    for (int i = 0; i < 3; i++)
    {
        arrG[i] = (int *)malloc(width * sizeof(int));
    }
    //Red temporary array
    int **arrR = (int **)malloc(3 * sizeof(int *));
    for (int i = 0; i < 3; i++)
    {
        arrR[i] = (int *)malloc(width * sizeof(int));
    }
    for (int i = 0; i < height; i++)
    {
        int left_bound, wide, high, sum;
        //Copy image into temp arrays
        if (i == 0)
        {
            for (int j = 0; j < TWO; j++)
                for (int k = 0; k < width; k++)
                {
                    arrB[j][k] = image[i + j][k].rgbtBlue;
                    arrG[j][k] = image[i + j][k].rgbtGreen;
                    arrR[j][k] = image[i + j][k].rgbtRed;
                }
        }
        else if (i == 1)
        {
            for (int j = 0; j < width; j++)
            {
                arrB[TWO][j] = image[TWO][j].rgbtBlue;
                arrG[TWO][j] = image[TWO][j].rgbtGreen;
                arrR[TWO][j] = image[TWO][j].rgbtRed;
            }
        }
        else if (i != height - 1)
        {
            //Copy from line 2 to line 1
            for (int j = 0; j < width; j++)
            {
                arrB[0][j] = arrB[1][j];
                arrG[0][j] = arrG[1][j];
                arrR[0][j] = arrR[1][j];
            }
            //Copy from line 3 to line 2
            for (int j = 0; j < width; j++)
            {
                arrB[1][j] = arrB[2][j];
                arrG[1][j] = arrG[2][j];
                arrR[1][j] = arrR[2][j];
            }
            //Copy new info into line 3
            for (int j = 0; j < width; j++)
            {
                arrB[2][j] = image[i + 1][j].rgbtBlue;
                arrG[2][j] = image[i + 1][j].rgbtGreen;
                arrR[2][j] = image[i + 1][j].rgbtRed;
            }
        }
        else //In the case it's the last line
        {
            //Copy from line 2 to line 1
            for (int j = 0; j < width; j++)
            {
                arrB[0][j] = arrB[1][j];
                arrG[0][j] = arrG[1][j];
                arrR[0][j] = arrR[1][j];
            }
            //Copy from line 3 to line 2
            for (int j = 0; j < width; j++)
            {
                arrB[1][j] = arrB[2][j];
                arrG[1][j] = arrG[2][j];
                arrR[1][j] = arrR[2][j];
            }
        }
        for (int j = 0; j < width; j++)
        {
            //Set vertical bounds
            if (i == 0)
            {
                high = 2;
            }
            else if (i == height - 1)
            {
                high = 2;
            }
            else
            {
                high = 3;
            }
            //Set horizontal bounds
            if (j == 0)
            {
                left_bound = 0;
                wide = 2;
            }
            else if (j == width - 1)
            {
                left_bound = -1;
                wide = 2;
            }
            else
            {
                left_bound = -1;
                wide = 3;
            }
            //Blue
            sum = 0;
            for (int k = 0; k < high; k++)
            {
                for (int l = 0; l < wide; l++)
                {
                    sum += arrB[k][j + left_bound + l];
                }
            }
            image[i][j].rgbtBlue = (int)round((float)sum / (wide * high));
            //Green
            sum = 0;
            for (int k = 0; k < high; k++)
            {
                for (int l = 0; l < wide; l++)
                {
                    sum += arrG[k][j + left_bound + l];
                }
            }
            image[i][j].rgbtGreen = (int)round((float)sum / (wide * high));
            //Red
            sum = 0;
            for (int k = 0; k < high; k++)
            {
                for (int l = 0; l < wide; l++)
                {
                    sum += arrR[k][j + left_bound + l];
                }
            }
            image[i][j].rgbtRed = (int)round((float)sum / (wide * high));
        }
    }
    free(arrB);
    free(arrG);
    free(arrR);

    return;
}
