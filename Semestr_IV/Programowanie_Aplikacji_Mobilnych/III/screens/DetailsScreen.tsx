import { RootStackParamList } from "@/app/(tabs)/index";
import { RouteProp } from "@react-navigation/native";
import { StyleSheet, Text, View } from "react-native";

type DetailsScreenRouteProp = RouteProp<RootStackParamList, "Details">;

type DetailsScreenProps = {
    route: DetailsScreenRouteProp;
};

export default function DetailsScreen({ route }: DetailsScreenProps) {
    const { title, description } = route.params;

    return (
        <View style={styles.container}>
            <Text style={styles.title}>{title}</Text>
            <Text>{description}</Text>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        padding: 20,
        backgroundColor: "#4a90e2",
    },
    title: {
        color: "white",
        fontSize: 20,
        fontWeight: "bold",
    },
});