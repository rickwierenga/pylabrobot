﻿.. currentmodule:: pylabrobot.liquid_handling

pylabrobot.liquid_handling.backends package
===========================================

Backends are used to communicate with liquid handling devices on a low level. This can be useful
when you want to have very low level control over the liquid handling device or want to use a
feature that is not yet implemented in the front end.

Abstract
--------

.. autosummary::
  :toctree: _autosummary
  :nosignatures:
  :recursive:

    pylabrobot.liquid_handling.backends.LiquidHandlerBackend

Hardware
--------

.. autosummary::
  :toctree: _autosummary
  :nosignatures:
  :recursive:

    pylabrobot.liquid_handling.backends.hamilton.HamiltonLiquidHandler
    pylabrobot.liquid_handling.backends.hamilton.STAR

Net
---

Net backends can be used to communicate with servers that manage liquid handling devices.

.. autosummary::
  :toctree: _autosummary
  :nosignatures:
  :recursive:

    pylabrobot.liquid_handling.backends.net.HTTPBackend
    pylabrobot.liquid_handling.backends.net.WebSocketBackend

Simulator
---------

.. autosummary::
  :toctree: _autosummary
  :nosignatures:
  :recursive:

    pylabrobot.liquid_handling.backends.simulation.SimulatorBackend
