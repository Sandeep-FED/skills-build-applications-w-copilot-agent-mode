import React, { useEffect, useState } from "react"

function Workouts() {
  const [workouts, setWorkouts] = useState([])

  useEffect(() => {
    fetch(
      "https://stunning-eureka-qp645v99w726xpp-8000.app.github.dev/api/workouts/"
    )
      .then((response) => response.json())
      .then((data) => setWorkouts(data))
      .catch((error) => console.error("Error fetching workouts:", error))
  }, [])

  return (
    <div className='container mt-4'>
      <h1 className='text-center'>Workouts</h1>
      <table className='table table-striped table-bordered mt-4'>
        <thead className='table-dark'>
          <tr>
            <th>Name</th>
            <th>Description</th>
          </tr>
        </thead>
        <tbody>
          {workouts.map((workout) => (
            <tr key={workout._id}>
              <td>{workout.name}</td>
              <td>{workout.description}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default Workouts
