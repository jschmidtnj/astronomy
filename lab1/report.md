# Lab 1 - Determining the Mass of Jupiter

*I pledge my honor that I have abided by the Stevens Honor System.* - Joshua Schmidt

Name: Joshua Schmidt, Date: 11/25/2020

## Introduction

The goal of this lab was to determine the mass of Jupiter through observing its moons. By using the Newtonian version of Kepler's third law, we can relate the orbital period (T) to the semimajor axis of orbit (R): $T^{2} = \frac{4 \cdot \pi ^{2}}{G  \cdot (M_{1} + M_{2})} \cdot R^{3}$. For low mass objects, this can be reduced to $T^{2} = \frac{4 \cdot \pi ^{2}}{G  \cdot M} \cdot R^{3}$. By plotting $T^{2}$ and $R^{3}$, one can determine the slope and use it to calculate the unknown mass.

## Data

The first step is to gather data for at least 15 moons. I decided to write everything in Python as opposed to in Excel. I used Beautiful Soup 4 to extract the table html tags from the wikipedia entry for Jupiter's moons (all of the source code can be found [here](https://github.com/jschmidtnj/astronomy/tree/main/lab1)). This is the link to the wikipedia entry, with the source data: [link](https://en.wikipedia.org/wiki/Moons_of_Jupiter#List). The data was then parsed into a Pandas dataframe and cleaned, removing text and converting the strings into numeric values. The output dataframe looks similar to what is shown below:

```txt
2020-11-25 22:23:02.399 | INFO     | __main__:main:28 - sample of data:

   order label       name        pronunciation  image abs.magn.                    diameter  ...
0      7   III  Ganymede  /ˈɡænɪmiːd/[49][50]    NaN      −2.1                      5262.4  ...
1      8    IV  Callisto          /kəˈlɪstoʊ/    NaN      −1.2                      4820.6  ...
2      5     I        Io              /ˈaɪoʊ/    NaN      −1.7  3643.2(3660 × 3637 × 3631)  ...
3      6    II    Europa      /jʊəˈroʊpə/[48]    NaN      −1.4                      3121.6  ...
4     11    VI   Himalia          /hɪˈmeɪliə/    NaN       7.9            139.6(150 × 120)  ...

semi-major_axis  orbital_period  inclination eccentricity discovery_year discoverer     group
    1070412000       618157.44    0.204[47]       0.0011           1610    Galilei  Galilean
    1882709000      1441929.60    0.205[47]       0.0074           1610    Galilei  Galilean
     421700000       152850.24    0.050[47]       0.0041           1610    Galilei  Galilean
     671034000       306823.68    0.471[47]       0.0094           1610    Galilei  Galilean
   11394100000     21467808.00       30.214       0.1510           1904    Perrine   Himalia
```

Here is a screenshot of the csv that is saved to disk (easier to read):

![Data Screenshot](output/data_screenshot.png)

\newpage

As you can see, there are many columns in this dataframe, and most are not being used. The only columns that are used are `name`, `semi-major_axis`, and `orbital_period`. The numeric columns are converted base SI units (meters and seconds). To avoid downloading the data every time the script is run, the dataframe is saved to disk.

## Plots

Below are the outputted plots from running the script:

![20 most massive moons](output/plot_20.png)

![4 Galileo moons](output/plot_4.png)

\newpage

## Calculation

Given the slope of the least square regression line, I used the following equation to calculate Jupiter's mass: $M = \frac{4 \cdot \pi^{2}}{G \cdot slope}$. The log output for the entire program can be found [here](https://github.com/jschmidtnj/astronomy/blob/main/lab1/output/logs.txt). $G$ is the gravitational constant, and the slope is 3.115590223034021e-16 for the 20 most massive moons and 3.115578858961228e-16 for the four Galileo moons.

## Comparison

The accepted mass of Jupiter is $1.89813 \cdot 10^{27} kg$. The estimation using 20 moons was 1.898513460916459e+27 kg, which is a slight overestimation. The estimation using Galileo's moons was 1.8985203857436408e+27 kg, which is also a slight overestimation, and is slightly further from the accepted value than the estimation with 20 moons. Both of these estimates are within 0.02% of the accepted value, which shows that this method for measuring the mass of Jupiter is very effective.

## Conclusion

In conclusion, this experiment was very successful, and I was able to accurately predict the mass of Jupiter. All of the code can be found on the aforementioned GitHub repository, and can be run through creating the anaconda environment (in `environment.yml`) and running the `src/main.py` file. The source code can also be downloaded with the following [link](https://github.com/jschmidtnj/astronomy/blob/main/lab1/lab1.zip).
