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
chapter_03/   Hodgkin-Huxley gating variables
chapter_04/   The Hodgkin-Huxley model
chapter_05/   RTM, Wang-Buzsaki, and Erisir models
chapter_07/   The leaky integrate-and-fire (LIF) model
chapter_08/   Quadratic and theta integrate-and-fire models
chapter_09/   Spike-frequency adaptation (AHP and M-current)
chapter_10/   2D reductions and phase-plane analysis
chapter_11/   Type I/II excitability and saddle-node bifurcations
chapter_12/   2D reduction of the RTM model, fixed-point stability
chapter_13/   The Hopf bifurcation
chapter_20/   Synapses
chapter_21/   Gap junctions
chapter_22/   The Wilson-Cowan equations
chapter_24/   Synchronization in networks of coupled oscillators
chapter_30/   PING (pyramidal-interneuron network gamma) rhythms
chapter_39/   Short-term synaptic plasticity
```

## Chapter Contents

| Chapter | Topic | Scripts |
|:---:|---|---|
| 3 | HH gating variables | `hh_gating_variables.py` |
| 4 | Hodgkin–Huxley model | `hodgkin_huxley_model.py` |
| 5 | RTM / WB / Erisir models | `rtm_voltage_trace.py`, `wb_voltage_trace.py`, `erisir_voltage_trace.py`, `three_models_gating_variables.py` |
| 7 | Leaky integrate-and-fire | `lif_voltage_trace.py`, `lif_neuron_with_hh.py` |
| 8 | Quadratic / theta integrate-and-fire | `qif_voltage_trace.py`, `qif_infinite_threshold.py`, `theta_firing.py` |
| 9 | Spike-frequency adaptation | `calcium_rise.py`, `m_current.py`, `lif_adapt.py`, `rtm_ahp.py`, `rtm_ahp_resting.py`, `rtm_m.py`, `rtm_m_resting.py`, `v_v_tilde.py` |
| 10 | 2D reductions & phase planes | `reduced_hh.py`, `hh_nullclines_plus_solution.py`, `hh_h_plus_n.py`, `hh_cycle_speed.py`, `fn.py` |
| 11 | Type I/II excitability | `saddle_node_bifurcation_1.py` |
| 12 | 2D RTM reduction & stability | `rtm_2d_fp.py`, `rtm_2d_invariant_cycle.py`, `rtm_2d_stability_analysis.py` |
| 13 | Hopf bifurcation | `hopf_sup_phase_plane.py`, `hopf_sub_phase_plane_1.py`, `hopf_sub_phase_plane_2.py`, `hopf_sup.py`, `hopf_sup_bif_diag.py`, `hopf_sup_bif_diag_1.py`, `hopf_sup_bif_diag_2.py` |
| 20 | Synapses | `b_jahr_stevens.py`, `rtm_plot_q.py`, `rtm_plot_s.py`, `rtm_plot_s_two_variables.py`, `rtm_plot_s_prescribe_tau_peak.py` |
| 21 | Gap junctions | `reset_threshold.py`, `wb_network_with_gj.py`, `wb_network_with_gj_subthreshold.py` |
| 22 | Wilson–Cowan equations | `wilson_cowan_e_and_i.py`, `wilson_cowan_phase_plane.py`, `wilson_cowan_phase_plane_1.py` |
| 24 | Network synchronization | `rtm_e_to_e_network_1.py`, `rtm_sync.py`, `rtm_splay.py` |
| 30 | PING rhythms | `ping_1.py` |
| 39 | Short-term synaptic plasticity | `rtm_with_depressing_s.py`, `rtm_with_depressing_and_facilitating_s.py`, `wb_with_depressing_s.py` |

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
python chapter_04/hodgkin_huxley_model.py
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
