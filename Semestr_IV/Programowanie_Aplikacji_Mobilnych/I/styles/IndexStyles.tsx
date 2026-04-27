import { StyleSheet } from "react-native";

export const styles = StyleSheet.create({
  detailsContainer: { 
    flex: 1, 
    padding: 20, 
    backgroundColor: '#4a90e2' 
  },
  detailsTitle: { 
    fontSize: 30,
    color: 'white', 
    fontWeight: 'bold', 
    marginBottom: 20, 
    textAlign: 'center' 
  },
  detailsInfoBox: { 
    backgroundColor: 'white', 
    borderRadius: 20, 
    padding: 20, 
    elevation: 5 
  },
  detailsLabel: { 
    fontSize: 14, 
    color: '#888', 
    fontWeight: 'bold', 
    marginTop: 10 
  },
  detailsValue: { 
    fontSize: 18, 
    color: '#333', 
    marginBottom: 5 
  },
});