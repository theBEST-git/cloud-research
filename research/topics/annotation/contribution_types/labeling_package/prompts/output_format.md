## Output format

Return ONLY a JSON object, with no prose before or after it and no code fences:

{"labels": [{"paper_id": "...", "primary_type": "...", "secondary_type": "...", "foundation_model": "...", "uncertain": false}]}

- Exactly one entry per paper in the request, in the same order. Copy each `paper_id` exactly as given.
- `primary_type`: one of `method`, `model`, `theory`, `empirical`, `system`, `dataset_benchmark`, `evaluation`,
  `problem`, `application`, `recipe`, `perspective`, `survey_position`.
- `secondary_type`: one of the same ids, or `none`. It must differ from `primary_type`; if the only candidate is the
  same type as the primary, use `none`.
- `foundation_model`: `yes` or `no`, by the foundation-model rule above.
- `uncertain`: `true` if the choice between two types (or the foundation-model call) was close, else `false`.
- Judge every paper from its title and abstract only. Label each paper independently of the others in the request.
