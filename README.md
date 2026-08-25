# An Introduction to Modeling Neuronal Dynamics — Code Reproductions

Python reproductions of the models, simulations, and figures from
**Christoph Börgers, *An Introduction to Modeling Neuronal Dynamics*
(Springer, 2017)**.

This repository was built as part of my B.Sc. project in Physics, working
through the book chapter by chapter and re-implementing its neuron and
network models from scratch — starting from single-compartment
conductance-based neurons (Hodgkin–Huxley, RTM, Wang–Buzsáki, Erisir),
through reduced and integrate-and-fire descriptions, phase-plane and
bifurcation analysis, synaptic transmission and short-term plasticity,
gap junctions, and finally network-level phenomena such as
synchronization and PING gamma rhythms.

## Repository Structure

Each folder corresponds to a chapter of the book. Every script is
self-contained (parameters, model equations, and plotting all in one
file) and opens with a docstring describing what it reproduces.

```
Chapter 1/    The Hodgkin-Huxley model (introductory reproduction)
Chapter 3/    Hodgkin-Huxley gating variables
Chapter 4/    The Hodgkin-Huxley model
Chapter 5/    RTM, Wang-Buzsaki, and Erisir models
Chapter 7/    The leaky integrate-and-fire (LIF) model
Chapter 8/    Quadratic and theta integrate-and-fire models
Chapter 9/    Spike-frequency adaptation (AHP and M-current)
Chapter 10/   2D reductions and phase-plane analysis
Chapter 11/   Type I/II excitability and saddle-node bifurcations
Chapter 12/   2D reduction of the RTM model, fixed-point stability
Chapter 13/   The Hopf bifurcation
Chapter 20/   Synapses
Chapter 21/   Gap junctions
Chapter 22/   The Wilson-Cowan equations
Chapter 24/   Synchronization in networks of coupled oscillators
Chapter 30/   PING (pyramidal-interneuron network gamma) rhythms
Chapter 39/   Short-term synaptic plasticity
```

## Chapter Contents

| Chapter | Topic | Scripts |
|:---:|---|---|
| 1 | Hodgkin-Huxley model (intro) | `HH_VOLTAGE_TRACE.py` |
| 3 | HH gating variables | `HH_GATING_VARIABLES.py` |
| 4 | Hodgkin–Huxley model | `Hodgkin-Huxley Model.py` |
| 5 | RTM / WB / Erisir models | `RTM_VOLTAGE_TRACE.py`, `WB_VOLTAGE_TRACE.py`, `ERISIR_VOLTAGE_TRACE.py`, `THREE_MODELS_GATING_VARIABLES.py` |
| 7 | Leaky integrate-and-fire | `LIF_VOLTAGE_TRACE.py`, `LIF_NEURON_WITH_HH.py` |
| 8 | Quadratic / theta integrate-and-fire | `QIF_VOLTAGE_TRACE.py`, `QIF_INFINITE_THRESHOLD.py`, `THETA_FIRING.py` |
| 9 | Spike-frequency adaptation | `CALCIUM_RISE.py`, `M_CURRENT.py`, `LIF_ADAPT.py`, `RTM_AHP.py`, `RTM_AHP_RESTING.py`, `RTM_M.py`, `RTM_M_RESTING.py`, `V_V_TILDE.py` |
| 10 | 2D reductions & phase planes | `REDUCED_HH.py`, `HH_NULLCLINES_PLUS_SOLUTION.py`, `HH_H_PLUS_N.py`, `HH_CYCLE_SPEED.py`, `FN.py` |
| 11 | Type I/II excitability | `SADDLE_NODE_BIFURCATION_1.py` |
| 12 | 2D RTM reduction & stability | `RTM_2D_FP.py`, `RTM_2D_INVARIANT_CYCLE.py`, `RTM_2D_STABILITY_ANALYSIS.py` |
| 13 | Hopf bifurcation | `HOPF_SUP_PHASE_PLANE.py`, `HOPF_SUB_PHASE_PLANE_1.py`, `HOPF_SUB_PHASE_PLANE_2.py`, `HOPF_SUP.py`, `HOPF_SUP_BIF_DIAG.py`, `HOPF_SUP_BIF_DIAG_1.py`, `HOPF_SUP_BIF_DIAG_2.py` |
| 20 | Synapses | `B_JAHR_STEVENS.py`, `RTM_PLOT_Q.py`, `RTM_PLOT_S.py`, `RTM_PLOT_S_TWO_VARIABLES.py`, `RTM_PLOT_S_PRESCRIBE_TAU_PEAK.py` |
| 21 | Gap junctions | `RESET_THRESHOLD.py`, `WB_NETWORK_WITH_GJ.py`, `WB_NETWORK_WITH_GJ_SUBTHRESHOLD.py` |
| 22 | Wilson–Cowan equations | `WILSON_COWAN_E_AND_I.py`, `WILSON_COWAN_PHASE_PLANE.py`, `WILSON_COWAN_PHASE_PLANE_1.py` |
| 24 | Network synchronization | `RTM_E_TO_E_NETWORK_1.py`, `RTM_SYNC.py`, `RTM_SPLAY.py` |
| 30 | PING rhythms | `PING_1.py` |
| 39 | Short-term synaptic plasticity | `RTM_WITH_DEPRESSING_S.py`, `RTM_WITH_DEPRESSING_AND_FACILITATING_S.py`, `WB_WITH_DEPRESSING_S.py` |

## Methods

Most single-neuron models are integrated either with a custom
4th-order Runge–Kutta solver or with `scipy.integrate.odeint`.
Fixed-point and stability analyses (Chapter 12) use automatic
differentiation via [autograd](https://github.com/HIPS/autograd) to
compute Jacobians directly from the model equations rather than
hand-derived linearizations.

## Requirements

- Python 3.9+
- `numpy`, `scipy`, `matplotlib`, `autograd`

Install with:

```bash
pip install -r requirements.txt
```

## Running

Each script is standalone and produces its plot(s) on execution, e.g.:

```bash
python "Chapter 4/Hodgkin-Huxley Model.py"
```

## Reference

Börgers, C. (2017). *An Introduction to Modeling Neuronal Dynamics.*
Texts in Applied Mathematics, vol. 66. Springer.

## Author

**Mahzad Jafari**
M.Sc. Physics Student, Institute for Advanced Studies in Basic Sciences (IASBS), Zanjan, Iran

[GitHub](https://github.com/mahjafari) &nbsp;|&nbsp; [LinkedIn](https://www.linkedin.com/in/mahzad-jafari)

## License

This code is released under the [MIT License](LICENSE). It is an
independent reproduction of models and figures described in Börgers'
textbook for educational purposes; the book's text and figures
themselves remain the copyright of the author and publisher.
