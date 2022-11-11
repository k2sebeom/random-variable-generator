from js import console, alert
from utils import plot_cdf, plot_density, plot, run

inp = Element('gu-input').element
btn = Element('run-button').element
trial_inp = Element('trials').element


def main(e):
    try:
        log, g = run(inp.value, eval(trial_inp.value))
        cdf = plot_cdf(log)
        dist = plot_density(log)
        gu = plot(g)
        Element('cdf').write(cdf)
        Element('dist').write(dist)
        Element('gU-plot').write(gu)
    except Exception as e:
        alert(e)

btn.onclick = main
