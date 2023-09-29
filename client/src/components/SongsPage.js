import React from 'react'
import { Route, useRouteMatch } from 'react-router-dom'
import SongsList from './SongsList'
import SongsShow from './SongsShow'
//import "./App.css";
//import SongForm from './SongForm'


function SongsPage({ songs, setSongs }) {
  const match = useRouteMatch();
  // console.log(match)



  return (
    <div>
       <h3>Choose a song from the list to see details</h3>
      <SongsList songs={songs} setSongs={setSongs}  />
      <Route exact path={match.url}>
       
      </Route>

      <Route path={`${match.url}/:songID`}>
        <SongsShow songs={songs} />
      </Route>
    </div>
  );
}

export default SongsPage