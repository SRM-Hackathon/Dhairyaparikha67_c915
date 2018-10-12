import {
  createStackNavigator,
} from 'react-navigation';

import Splash from './components/Splash'
import MainScreen from './components/MainScreen'


const App = createStackNavigator({
  Splash: { screen: Splash },
  MainScreen:{screen:MainScreen}
});

export default App;