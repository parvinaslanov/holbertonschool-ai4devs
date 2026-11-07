# User Stories & Acceptance Criteria

### User Story 1
As a corporate employee, I want to sign up using my work email so that I am verified as a trusted company commuter.
**Acceptance Criteria**:
- System validates domain against whitelist of approved enterprise domains.
- Verification link is sent to user email upon registration.
- Account remains pending until email link is verified.
**Priority**: MVP

### User Story 2
As a driver, I want to post a recurring or one-off commute schedule so that colleagues can book available seats in my car.
**Acceptance Criteria**:
- Driver can set departure time, pickup points, destination, and available seat count.
- Driver can flag schedule as single-day or repeating weekly.
- Schedule instantly becomes searchable in the ride-matching engine.
**Priority**: MVP

### User Story 3
As a passenger, I want to search for rides by pickup location, destination, and work schedule so that I can find a suitable route.
**Acceptance Criteria**:
- User enters origin, destination, and desired arrival time window.
- System displays matching drivers ranked by proximity and schedule overlap.
- User can view driver profile details and seat availability before requesting.
**Priority**: MVP

### User Story 4
As a passenger, I want to send a ride request to a driver so that I can secure my seat for the commute.
**Acceptance Criteria**:
- Passenger sends request with preferred pickup spot and time.
- Driver receives immediate push notification and email.
- Request expires automatically if unanswered within 30 minutes.
**Priority**: MVP

### User Story 5
As a driver, I want to accept or reject passenger requests so that I retain full control over who joins my carpool.
**Acceptance Criteria**:
- Driver sees requester profile, department, and route match rating.
- Accepting reserves the seat and sends confirmation to passenger.
- Rejecting notifies passenger and suggests alternative rides.
**Priority**: MVP

### User Story 6
As a passenger, I want ride expenses to be calculated automatically so that cost-sharing is transparent and hassle-free.
**Acceptance Criteria**:
- System calculates total trip cost using distance, current fuel prices, and toll rates.
- Cost is split equally among all confirmed occupants.
- Fare breakdown is visible to driver and passengers prior to ride confirmation.
**Priority**: High

### User Story 7
As a user, I want to rate and review co-workers after completing a ride so that accountability and community trust remain high.
**Acceptance Criteria**:
- Rating prompt appears upon completion of ride.
- Rating scale is 1–5 stars with optional tag selection (Punctual, Safe Driver, Pleasant).
- Ratings are visible on public internal profiles after at least 3 reviews are submitted.
**Priority**: High

### User Story 8
As an employee, I want to view my individual carbon footprint reduction metrics so that I can track my environmental contribution.
**Acceptance Criteria**:
- Dashboard displays cumulative distance carpooled and estimated CO₂ saved in kg.
- User can view personal stats weekly, monthly, and overall.
- User can export summary as a shareable badge or report.
**Priority**: Medium

### User Story 9
As a corporate administrator, I want to access an analytics dashboard so that I can monitor company-wide parking and sustainability impact.
**Acceptance Criteria**:
- Admin can view total rides completed, unique participants, and reduced parking strain.
- Admin can export monthly sustainability reports for corporate ESG compliance.
- Data is aggregated and anonymized to protect individual employee privacy.
**Priority**: Medium

### User Story 10
As a driver, I want to set preferred pickup waypoints along my route so that I don't have to make major detours.
**Acceptance Criteria**:
- Driver adds up to 3 custom pickup nodes on their base commute map.
- Matching algorithm prioritizes passengers located within 5 minutes of defined waypoints.
- System calculates and displays detour duration added per passenger pick-up.
**Priority**: Low
