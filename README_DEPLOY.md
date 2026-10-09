# Render demonstration deployment

This is a **test-data-only university demonstration**, not a payment-processing website. Donation submissions record simulated donations; **no money is collected**. Do not enter real donor details.

## Deploy
1. Upload these files to a new GitHub repository (do not upload `.env`, `instance/`, or credentials).
2. At https://dashboard.render.com select **New > Blueprint**, connect GitHub and select the repository. Render reads `render.yaml`.
3. Deploy and visit the Render URL. Check `/health` for `{"status":"ok"}`.
4. Registration is available at `/register`. Admin account creation at `/add-user` requires an existing admin account; for a demo you can show member and donation flows without admin access.

## Important limitations
- Render free web services have an ephemeral filesystem. Default SQLite records **will be lost** on restart/redeploy. Use disposable test records only.
- For persistent data, provision a PostgreSQL database separately and set `DATABASE_URL` on the web service. `db.create_all()` creates missing tables, not migrations.
- The original donation form did not connect to a payment provider and must **not** be represented as a real payment.
- This is a demo hardening pass, **not** a production security audit. The original forms have not been fully reviewed for CSRF, authorization, and abuse protection. Keep it test-only.
- Do not publish real credentials or personal donor/member information.
