---
status: Proposed
title: 'Fixed material, variable usable capacity: one sheet of area 8 folded into k accordion panels fits a stowage footprint of 2 only when k is at least 4, supplies the required functional area of 6 only when unfolded, and carries the required load only when k is at most 8, so packing, deployment and load capacity select different designs from the same inventory'
version: 1
standing: fictional
kind: construction
tags:
- operations-research
- mathematics
- society-and-governance
date: '2026-11-05'
line:
- distributed-agency
illustrates:
- CLAIM-296
summary: >-
  A's proposal, from the pasted synthesis on constraint architectures
  (pasted by the owner on 2026-11-04, continuing the exchange on emergency
  readiness whose share link could not be fetched), Part 4: an
  inextensible sheet has a fixed amount of material, and folding changes
  its footprint, volume, stiffness and functional area, so "A fold
  pattern converts the same physical inventory into different usable
  capacities." A gives the constraints A_material(z) ≤ B_material,
  V_stowed(z) ≤ B_storage and P_deployed(q,z) ≥ P_required without
  numbers; the numbers, and the stipulated load rule, are the filer's.
  One sheet of area 8 meets the material budget in every configuration,
  meets the stowage budget only folded and the area requirement only
  unfolded, and the tightest packing fails the load requirement. A's
  heavy-rescue reading: a company standing by and dispatched has the same
  inventory in a different configuration. The construction is the
  filer's, from A's fixed-material resource model; adopting it is the
  owner's call.
---
<!-- inactive-ok-file: LIT-tmp31xwy — Unfetched; the 2026 study A cites for the packing–load trade-off, unread and its identification unconfirmed, named only as A's citation -->

# CASE-tmp0s6cg: Fixed material, variable usable capacity: one sheet of area 8 folded into k accordion panels fits a stowage footprint of 2 only when k is at least 4, supplies the required functional area of 6 only when unfolded, and carries the required load only when k is at most 8, so packing, deployment and load capacity select different designs from the same inventory

## The case

**A's model.** A: "An inextensible sheet has approximately fixed surface
area", and "Folding changes neither the amount of material nor the total
area of the sheet. But it can radically change its deployed footprint,
occupied volume, stiffness, and functional surface area." With z the
fold pattern and q the configuration, A's constraints are

  A_material(z) ≤ B_material,  V_stowed(z) ≤ B_storage,  P_deployed(q,z) ≥ P_required.

For a deployable array, "The material needed for a large deployed array
is already present during launch; the resource constraint is that it
must initially fit within the spacecraft's limited stowage envelope."
A cites a solar-array source the record has not identified; nothing here
rests on it.

**The filer's numbers.** A sheet 1 × 8, of area 8 and panel thickness
0.01, folded as an accordion of k equal panels (fold radii ignored).

- **Material.** The area is 8 in every configuration and every k; the
  budget B_material = 8 is met throughout.
- **Stowage.** Folded flat, the stack has footprint 8/k and height
  0.01k. The envelope allows footprint ≤ 2 and height ≤ 0.1, so the
  sheet stows exactly when 4 ≤ k ≤ 10.
- **Function.** Unfolded, the exposed area is 8 against a required 6.
  Folded, only the top panel is exposed, 8/k ≤ 2. So no configuration
  meets the stowage and function requirements at once: the sheet meets
  them at different times, and the move between them is the deployment.
- **Load (a stipulated rule, the filer's).** Let the deployed array's
  load capacity be 4/k, falling with the number of creases, against a
  requirement of 0.5. It is met exactly when k ≤ 8.

So the designs that stow, deploy to the required area and carry the load
are k = 4, …, 8. The tightest packing, k = 10, footprint 0.8, carries
0.4 and fails. Checked by the filer.

## What it can show

- **That quantity does not fix capability.** Every design and every
  configuration holds the same 8 units of material. What changes between
  them is footprint, exposed area and load capacity, each set by the
  arrangement. A: "A resource can be present without being deployed, and
  deployment can change its effective function without changing its
  quantity." This is the point of [CLAIM-296](../claims.d/CLAIM-296.md), that what a system has and
  what it can deploy are different, made with a single inventory.
- **That packing, deployment and load are separate objectives.** A: "a
  design optimized for compact storage may be poor at carrying loads",
  and "we should not treat packing efficiency, deployment capability, and
  operational resilience as one objective." Here maximizing packing picks
  k = 10, and the load requirement excludes it. A attributes the warning
  to a 2026 study, held as [LIT-tmp31xwy](../literature.d/LIT-tmp31xwy.md) and not read; the construction
  does not rest on it.
- **A's organizational reading.** A: "A fully equipped rescue company has
  a latent technical capability when standing by. When dispatched, it
  reallocates that capability toward a particular incident. It hasn't
  acquired a new inventory of tools or expertise; it has changed the
  operational configuration in which they are available." Standing by is
  the stowed configuration, dispatch the deployment; whether the
  equipment is available for a task by its deadline is [TERM-055](../terms.d/TERM-055.md)'s
  operational availability, not its count.

## What it cannot show

- **Anything about real sheets or arrays.** The load rule 4/k is
  invented to put the packing and load requirements in conflict; real
  stiffness depends on crease mechanics the case leaves out.
- **That deployment is possible or cheap.** The case compares
  configurations; the path from stowed to deployed, its peak resource
  need and its reliability are not modelled.
- **That an organization's "inventory" is fixed** the way a sheet's area
  is. Staff and skills decay and turn over; the analogy holds only for
  what is held fixed.
