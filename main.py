from js import console, alert
from utils import plot_cdf, plot_density, run

inp = Element('gu-input').element
btn = Element('run-button').element
trial_inp = Element('trials').element


def main(e):
    try:
        log = run(inp.value, eval(trial_inp.value))
        cdf = plot_cdf(log)
        dist = plot_density(log)
        Element('cdf').write(cdf)
        Element('dist').write(dist)
    except Exception as e:
        alert(e)


btn.onclick = main
